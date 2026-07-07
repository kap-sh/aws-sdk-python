"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#AddStreamGroupLocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.identifier
    import aws_sdk_gameliftstreams.types.location_configurations


class AddStreamGroupLocationsInput(TypedDict, closed=True):
    identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier"
    r"""<p> A stream group to add the specified locations to. </p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    location_configurations: (
        "aws_sdk_gameliftstreams.types.location_configurations.LocationConfigurations"
    )
    """<p> A set of one or more locations and the streaming capacity for each location. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddStreamGroupLocationsInput) -> dict:
    out: dict = {}
    import aws_sdk_gameliftstreams.types.location_configurations

    out["LocationConfigurations"] = (
        aws_sdk_gameliftstreams.types.location_configurations.serialize_json(
            value["location_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddStreamGroupLocationsInput:
    out: AddStreamGroupLocationsInput = {}  # type: ignore[typeddict-item]
    if "LocationConfigurations" in data:
        import aws_sdk_gameliftstreams.types.location_configurations

        out["location_configurations"] = (
            aws_sdk_gameliftstreams.types.location_configurations.deserialize_json(
                data["LocationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "AddStreamGroupLocationsInput.location_configurations required"
        )
    return out
