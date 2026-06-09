"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRoleResponse``."""

from typing import TypedDict

from aws_sdk_iam._protocol.xml import Element


class UpdateRoleResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UpdateRoleResponse:
    out: UpdateRoleResponse = {}  # type: ignore[typeddict-item]
    return out
