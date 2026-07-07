"""Generated from Smithy shape ``com.amazonaws.ivs#DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.s3_destination_configuration


class DestinationConfiguration(TypedDict, closed=True):
    s3: NotRequired[
        "aws_sdk_ivs.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>An S3 destination configuration where recorded videos will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_ivs.types.s3_destination_configuration

        out["s3"] = aws_sdk_ivs.types.s3_destination_configuration.serialize_json(
            value["s3"]
        )
    return out


def deserialize_json(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import aws_sdk_ivs.types.s3_destination_configuration

        out["s3"] = aws_sdk_ivs.types.s3_destination_configuration.deserialize_json(
            data["s3"]
        )
    return out
