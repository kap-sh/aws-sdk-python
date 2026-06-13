"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#DestinationConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.s3_destination


class DestinationConfigurations(TypedDict):
    s3_destination: "aws_sdk_bcm_data_exports.types.s3_destination.S3Destination"
    """<p>An object that describes the destination of the data exports file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationConfigurations) -> dict:
    out: dict = {}
    import aws_sdk_bcm_data_exports.types.s3_destination

    out["S3Destination"] = (
        aws_sdk_bcm_data_exports.types.s3_destination.serialize_aws_json_1_1(
            value["s3_destination"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationConfigurations:
    out: DestinationConfigurations = {}  # type: ignore[typeddict-item]
    if "S3Destination" in data:
        import aws_sdk_bcm_data_exports.types.s3_destination

        out["s3_destination"] = (
            aws_sdk_bcm_data_exports.types.s3_destination.deserialize_aws_json_1_1(
                data["S3Destination"]
            )
        )
    else:
        raise DeserializationError("DestinationConfigurations.s3_destination required")
    return out
