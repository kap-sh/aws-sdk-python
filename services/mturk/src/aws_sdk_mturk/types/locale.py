"""Generated from Smithy shape ``com.amazonaws.mturk#Locale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.country_parameters


class Locale(TypedDict, closed=True):
    country: "aws_sdk_mturk.types.country_parameters.CountryParameters"
    """<p> The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America. </p>"""
    subdivision: NotRequired["aws_sdk_mturk.types.country_parameters.CountryParameters"]
    """<p>The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Locale) -> dict:
    out: dict = {}
    out["Country"] = value["country"]
    if "subdivision" in value:
        out["Subdivision"] = value["subdivision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Locale:
    out: Locale = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    else:
        raise DeserializationError("Locale.country required")
    if "Subdivision" in data:
        out["subdivision"] = data["Subdivision"]
    return out
