"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningPolicyBuildResultAssetType: TypeAlias = Literal[
    "BUILD_LOG",
    "QUALITY_REPORT",
    "POLICY_DEFINITION",
    "GENERATED_TEST_CASES",
    "POLICY_SCENARIOS",
    "FIDELITY_REPORT",
    "ASSET_MANIFEST",
    "SOURCE_DOCUMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD_LOG",
        "QUALITY_REPORT",
        "POLICY_DEFINITION",
        "GENERATED_TEST_CASES",
        "POLICY_SCENARIOS",
        "FIDELITY_REPORT",
        "ASSET_MANIFEST",
        "SOURCE_DOCUMENT",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildResultAssetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildResultAssetType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildResultAssetType, data)
