"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CustomWorkspaceImageImportState: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "PROCESSING_SOURCE_IMAGE",
    "IMAGE_TESTING_START",
    "UPDATING_OPERATING_SYSTEM",
    "IMAGE_COMPATIBILITY_CHECKING",
    "IMAGE_TESTING_GENERALIZATION",
    "CREATING_TEST_INSTANCE",
    "INSTALLING_COMPONENTS",
    "GENERALIZING",
    "VALIDATING",
    "PUBLISHING",
    "COMPLETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "PROCESSING_SOURCE_IMAGE",
        "IMAGE_TESTING_START",
        "UPDATING_OPERATING_SYSTEM",
        "IMAGE_COMPATIBILITY_CHECKING",
        "IMAGE_TESTING_GENERALIZATION",
        "CREATING_TEST_INSTANCE",
        "INSTALLING_COMPONENTS",
        "GENERALIZING",
        "VALIDATING",
        "PUBLISHING",
        "COMPLETED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: CustomWorkspaceImageImportState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomWorkspaceImageImportState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomWorkspaceImageImportState value: {data!r}"
        )
    return cast(CustomWorkspaceImageImportState, data)
