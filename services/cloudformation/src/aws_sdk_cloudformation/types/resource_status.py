"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

ResourceStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "CREATE_COMPLETE",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_COMPLETE",
    "DELETE_SKIPPED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_COMPLETE",
    "IMPORT_FAILED",
    "IMPORT_COMPLETE",
    "IMPORT_IN_PROGRESS",
    "IMPORT_ROLLBACK_IN_PROGRESS",
    "IMPORT_ROLLBACK_FAILED",
    "IMPORT_ROLLBACK_COMPLETE",
    "EXPORT_FAILED",
    "EXPORT_COMPLETE",
    "EXPORT_IN_PROGRESS",
    "EXPORT_ROLLBACK_IN_PROGRESS",
    "EXPORT_ROLLBACK_FAILED",
    "EXPORT_ROLLBACK_COMPLETE",
    "UPDATE_ROLLBACK_IN_PROGRESS",
    "UPDATE_ROLLBACK_COMPLETE",
    "UPDATE_ROLLBACK_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: ResourceStatus) -> str:
    return value


def from_query_text(text: str) -> ResourceStatus:
    return cast(ResourceStatus, text)


def serialize_query(
    value: ResourceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceStatus:
    return from_query_text(el.text or "")
