"""Generated from Smithy shape ``com.amazonaws.identitystore#Address``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.boolean_type
    import aws_sdk_identitystore.types.sensitive_string_type


class Address(TypedDict):
    street_address: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The street of the address.</p>"""
    locality: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string of the address locality.</p>"""
    region: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The region of the address.</p>"""
    postal_code: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The postal code of the address.</p>"""
    country: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The country of the address.</p>"""
    formatted: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a formatted version of the address for display.</p>"""
    type: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    r"""<p>A string representing the type of address. For example, \"Home.\"</p>"""
    primary: "aws_sdk_identitystore.types.boolean_type.BooleanType"
    """<p>A Boolean value representing whether this is the primary address for the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Address) -> dict:
    out: dict = {}
    if "street_address" in value:
        out["StreetAddress"] = value["street_address"]
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "region" in value:
        out["Region"] = value["region"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "country" in value:
        out["Country"] = value["country"]
    if "formatted" in value:
        out["Formatted"] = value["formatted"]
    if "type" in value:
        out["Type"] = value["type"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if "StreetAddress" in data:
        out["street_address"] = data["StreetAddress"]
    if "Locality" in data:
        out["locality"] = data["Locality"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Formatted" in data:
        out["formatted"] = data["Formatted"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out
