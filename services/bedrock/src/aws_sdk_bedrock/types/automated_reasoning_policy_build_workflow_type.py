"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningPolicyBuildWorkflowType: TypeAlias = Literal[
    "INGEST_CONTENT",
    "REFINE_POLICY",
    "IMPORT_POLICY",
    "GENERATE_FIDELITY_REPORT",
    "GENERATE_POLICY_SCENARIOS",
    "RESOLVE_POLICY_AMBIGUITIES",
    "ITERATIVELY_REFINE_POLICY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INGEST_CONTENT",
        "REFINE_POLICY",
        "IMPORT_POLICY",
        "GENERATE_FIDELITY_REPORT",
        "GENERATE_POLICY_SCENARIOS",
        "RESOLVE_POLICY_AMBIGUITIES",
        "ITERATIVELY_REFINE_POLICY",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildWorkflowType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildWorkflowType, data)
