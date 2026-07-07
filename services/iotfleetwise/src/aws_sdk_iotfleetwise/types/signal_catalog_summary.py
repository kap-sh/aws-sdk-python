"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalCatalogSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.string
    import aws_sdk_iotfleetwise.types.timestamp


class SignalCatalogSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>The name of the signal catalog.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the signal catalog.</p>"""
    creation_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: NotRequired[
        "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    ]
    """<p>The time the signal catalog was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalCatalogSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_modification_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalCatalogSummary:
    out: SignalCatalogSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    return out
