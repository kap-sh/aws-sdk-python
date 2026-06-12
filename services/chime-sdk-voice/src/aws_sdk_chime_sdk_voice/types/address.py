"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Address``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string


class Address(TypedDict):
    street_name: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The address street, such as <code>8th Avenue</code>.</p>"""
    street_suffix: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The address suffix, such as the <code>N</code> in <code>8th Avenue N</code>.</p>"""
    post_directional: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>An address suffix location, such as the <code>S. Unit A</code> in <code>Central Park S. Unit A</code>.</p>"""
    pre_directional: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>An address prefix location, such as the <code>N</code> in <code>N. Third St.</code> </p>"""
    street_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The numeric portion of an address.</p>"""
    city: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The city of an address.</p>"""
    state: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The state of an address.</p>"""
    postal_code: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The postal code of an address.</p>"""
    postal_code_plus4: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The zip + 4 or postal code + 4 of an address.</p>"""
    country: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The country of an address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    if "street_name" in value:
        out["streetName"] = value["street_name"]
    if "street_suffix" in value:
        out["streetSuffix"] = value["street_suffix"]
    if "post_directional" in value:
        out["postDirectional"] = value["post_directional"]
    if "pre_directional" in value:
        out["preDirectional"] = value["pre_directional"]
    if "street_number" in value:
        out["streetNumber"] = value["street_number"]
    if "city" in value:
        out["city"] = value["city"]
    if "state" in value:
        out["state"] = value["state"]
    if "postal_code" in value:
        out["postalCode"] = value["postal_code"]
    if "postal_code_plus4" in value:
        out["postalCodePlus4"] = value["postal_code_plus4"]
    if "country" in value:
        out["country"] = value["country"]
    return out


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if "streetName" in data:
        out["street_name"] = data["streetName"]
    if "streetSuffix" in data:
        out["street_suffix"] = data["streetSuffix"]
    if "postDirectional" in data:
        out["post_directional"] = data["postDirectional"]
    if "preDirectional" in data:
        out["pre_directional"] = data["preDirectional"]
    if "streetNumber" in data:
        out["street_number"] = data["streetNumber"]
    if "city" in data:
        out["city"] = data["city"]
    if "state" in data:
        out["state"] = data["state"]
    if "postalCode" in data:
        out["postal_code"] = data["postalCode"]
    if "postalCodePlus4" in data:
        out["postal_code_plus4"] = data["postalCodePlus4"]
    if "country" in data:
        out["country"] = data["country"]
    return out
