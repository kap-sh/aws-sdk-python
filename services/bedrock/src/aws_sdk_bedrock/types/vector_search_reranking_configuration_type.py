"""Generated from Smithy shape ``com.amazonaws.bedrock#VectorSearchRerankingConfigurationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

VectorSearchRerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BEDROCK_RERANKING_MODEL",))


def serialize_json(value: VectorSearchRerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> VectorSearchRerankingConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VectorSearchRerankingConfigurationType value: {data!r}"
        )
    return cast(VectorSearchRerankingConfigurationType, data)
