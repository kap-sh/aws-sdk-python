"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterDeploymentType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_timestream_influxdb.errors import DeserializationError
from aws_sdk_timestream_influxdb._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ClusterDeploymentType: TypeAlias = Literal["MULTI_NODE_READ_REPLICAS",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("MULTI_NODE_READ_REPLICAS",))


def serialize_aws_json_1_0(value: ClusterDeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterDeploymentType value: {data!r}")
    return cast(ClusterDeploymentType, data)