"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpgradePublishedSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class UpgradePublishedSchemaResponse(TypedDict):
    upgraded_schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN of the upgraded schema that is returned as part of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradePublishedSchemaResponse) -> dict:
    out: dict = {}
    if "upgraded_schema_arn" in value:
        out["UpgradedSchemaArn"] = value["upgraded_schema_arn"]
    return out


def deserialize_json(data: dict) -> UpgradePublishedSchemaResponse:
    out: UpgradePublishedSchemaResponse = {}  # type: ignore[typeddict-item]
    if "UpgradedSchemaArn" in data:
        out["upgraded_schema_arn"] = data["UpgradedSchemaArn"]
    return out
