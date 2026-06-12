"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteLocationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.custom_location_name_or_arn_model


class DeleteLocationInput(TypedDict):
    location_name: NotRequired[
        "aws_sdk_gamelift.types.custom_location_name_or_arn_model.CustomLocationNameOrArnModel"
    ]
    """<p>The location name of the custom location to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLocationInput) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLocationInput:
    out: DeleteLocationInput = {}  # type: ignore[typeddict-item]
    if "LocationName" in data:
        out["location_name"] = data["LocationName"]
    return out
