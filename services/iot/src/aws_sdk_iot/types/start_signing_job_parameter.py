"""Generated from Smithy shape ``com.amazonaws.iot#StartSigningJobParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.destination
    import aws_sdk_iot.types.signing_profile_name
    import aws_sdk_iot.types.signing_profile_parameter


class StartSigningJobParameter(TypedDict, closed=True):
    signing_profile_parameter: NotRequired[
        "aws_sdk_iot.types.signing_profile_parameter.SigningProfileParameter"
    ]
    """<p>Describes the code-signing profile.</p>"""
    signing_profile_name: NotRequired[
        "aws_sdk_iot.types.signing_profile_name.SigningProfileName"
    ]
    """<p>The code-signing profile name.</p>"""
    destination: NotRequired["aws_sdk_iot.types.destination.Destination"]
    """<p>The location to write the code-signed file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSigningJobParameter) -> dict:
    out: dict = {}
    if "signing_profile_parameter" in value:
        import aws_sdk_iot.types.signing_profile_parameter

        out["signingProfileParameter"] = (
            aws_sdk_iot.types.signing_profile_parameter.serialize_json(
                value["signing_profile_parameter"]
            )
        )
    if "signing_profile_name" in value:
        out["signingProfileName"] = value["signing_profile_name"]
    if "destination" in value:
        import aws_sdk_iot.types.destination

        out["destination"] = aws_sdk_iot.types.destination.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> StartSigningJobParameter:
    out: StartSigningJobParameter = {}  # type: ignore[typeddict-item]
    if "signingProfileParameter" in data:
        import aws_sdk_iot.types.signing_profile_parameter

        out["signing_profile_parameter"] = (
            aws_sdk_iot.types.signing_profile_parameter.deserialize_json(
                data["signingProfileParameter"]
            )
        )
    if "signingProfileName" in data:
        out["signing_profile_name"] = data["signingProfileName"]
    if "destination" in data:
        import aws_sdk_iot.types.destination

        out["destination"] = aws_sdk_iot.types.destination.deserialize_json(
            data["destination"]
        )
    return out
