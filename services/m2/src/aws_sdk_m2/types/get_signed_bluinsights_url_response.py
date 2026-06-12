"""Generated from Smithy shape ``com.amazonaws.m2#GetSignedBluinsightsUrlResponse``."""

from typing import TypedDict

from aws_sdk_m2.errors import DeserializationError


class GetSignedBluinsightsUrlResponse(TypedDict):
    signed_bi_url: "str"
    """<p>Single sign-on AWS Blu Insights URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSignedBluinsightsUrlResponse) -> dict:
    out: dict = {}
    out["signedBiUrl"] = value["signed_bi_url"]
    return out


def deserialize_json(data: dict) -> GetSignedBluinsightsUrlResponse:
    out: GetSignedBluinsightsUrlResponse = {}  # type: ignore[typeddict-item]
    if "signedBiUrl" in data:
        out["signed_bi_url"] = data["signedBiUrl"]
    else:
        raise DeserializationError(
            "GetSignedBluinsightsUrlResponse.signed_bi_url required"
        )
    return out
