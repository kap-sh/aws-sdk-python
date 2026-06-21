"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

DeploymentMode: TypeAlias = Literal["REVERT_DRIFT",]


# --- awsQuery ser/de ---
def to_query_text(value: DeploymentMode) -> str:
    return value


def from_query_text(text: str) -> DeploymentMode:
    return cast(DeploymentMode, text)


def serialize_query(
    value: DeploymentMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeploymentMode:
    return from_query_text(el.text or "")
