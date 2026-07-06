"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateLocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_model


class CreateLocationOutput(TypedDict, closed=True):
    location: NotRequired["aws_sdk_gamelift.types.location_model.LocationModel"]
    """<p>The details of the custom location you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationOutput) -> dict:
    out: dict = {}
    if "location" in value:
        import aws_sdk_gamelift.types.location_model

        out["Location"] = aws_sdk_gamelift.types.location_model.serialize_aws_json_1_1(
            value["location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationOutput:
    out: CreateLocationOutput = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        import aws_sdk_gamelift.types.location_model

        out["location"] = (
            aws_sdk_gamelift.types.location_model.deserialize_aws_json_1_1(
                data["Location"]
            )
        )
    return out
