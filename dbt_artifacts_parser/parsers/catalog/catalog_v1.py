# generated by datamodel-codegen:
#   filename:  catalog_v1.json

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import ConfigDict, Field

from dbt_artifacts_parser.parsers.base import BaseParserModel


class CatalogMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dbt_schema_version: Optional[str] = 'https://schemas.getdbt.com/dbt/catalog/v1.json'
    dbt_version: Optional[str] = '0.19.0'
    generated_at: Optional[datetime] = '2021-02-10T04:42:33.680487Z'
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = {}


class TableMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: str
    database: Optional[str] = None
    schema_: str = Field(..., alias='schema')
    name: str
    comment: Optional[str] = None
    owner: Optional[str] = None


class ColumnMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: str
    comment: Optional[str] = None
    index: int
    name: str


class StatsItem(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: str
    label: str
    value: Optional[Union[bool, str, float]] = None
    description: Optional[str] = None
    include: bool


class CatalogTable(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    metadata: TableMetadata
    columns: Dict[str, ColumnMetadata]
    stats: Dict[str, StatsItem]
    unique_id: Optional[str] = None


class CatalogV1(BaseParserModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    metadata: CatalogMetadata
    nodes: Dict[str, CatalogTable]
    sources: Dict[str, CatalogTable]
    errors: Optional[List[str]] = None
