"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.aggregated_profile


class GetProfileResponse(TypedDict):
    profile: "aws_sdk_codeguruprofiler.types.aggregated_profile.AggregatedProfile"
    """<p>Information about the profile.</p>"""
    content_type: "str"
    """<p>The content type of the profile in the payload. It is either <code>application/json</code> or the default <code>application/x-amzn-ion</code>.</p>"""
    content_encoding: NotRequired["str"]
    """<p>The content encoding of the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.aggregated_profile

    out["profile"] = aws_sdk_codeguruprofiler.types.aggregated_profile.serialize_json(
        value["profile"]
    )
    return out


def deserialize_json(data: dict) -> GetProfileResponse:
    out: GetProfileResponse = {}  # type: ignore[typeddict-item]
    if "profile" in data:
        import aws_sdk_codeguruprofiler.types.aggregated_profile

        out["profile"] = (
            aws_sdk_codeguruprofiler.types.aggregated_profile.deserialize_json(
                data["profile"]
            )
        )
    else:
        raise DeserializationError("GetProfileResponse.profile required")
    return out
