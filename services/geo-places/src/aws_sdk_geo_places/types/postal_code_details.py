"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalCodeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.postal_authority
    import aws_sdk_geo_places.types.postal_code_type
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.usps_zip
    import aws_sdk_geo_places.types.usps_zip_plus4


class PostalCodeDetails(TypedDict):
    postal_code: NotRequired[
        "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess. </p>"""
    postal_authority: NotRequired[
        "aws_sdk_geo_places.types.postal_authority.PostalAuthority"
    ]
    """<p>The postal authority or entity. This could be a governmental authority, a regulatory authority, or a designated postal operator.</p>"""
    postal_code_type: NotRequired[
        "aws_sdk_geo_places.types.postal_code_type.PostalCodeType"
    ]
    """<p>The postal code type.</p>"""
    usps_zip: NotRequired["aws_sdk_geo_places.types.usps_zip.UspsZip"]
    """<p>The ZIP Classification Code, or in other words what type of postal code is it.</p>"""
    usps_zip_plus4: NotRequired["aws_sdk_geo_places.types.usps_zip_plus4.UspsZipPlus4"]
    """<p>The USPS ZIP+4 Record Type Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostalCodeDetails) -> dict:
    out: dict = {}
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "postal_authority" in value:
        out["PostalAuthority"] = value["postal_authority"]
    if "postal_code_type" in value:
        out["PostalCodeType"] = value["postal_code_type"]
    if "usps_zip" in value:
        import aws_sdk_geo_places.types.usps_zip

        out["UspsZip"] = aws_sdk_geo_places.types.usps_zip.serialize_json(
            value["usps_zip"]
        )
    if "usps_zip_plus4" in value:
        import aws_sdk_geo_places.types.usps_zip_plus4

        out["UspsZipPlus4"] = aws_sdk_geo_places.types.usps_zip_plus4.serialize_json(
            value["usps_zip_plus4"]
        )
    return out


def deserialize_json(data: dict) -> PostalCodeDetails:
    out: PostalCodeDetails = {}  # type: ignore[typeddict-item]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    if "PostalAuthority" in data:
        out["postal_authority"] = data["PostalAuthority"]
    if "PostalCodeType" in data:
        out["postal_code_type"] = data["PostalCodeType"]
    if "UspsZip" in data:
        import aws_sdk_geo_places.types.usps_zip

        out["usps_zip"] = aws_sdk_geo_places.types.usps_zip.deserialize_json(
            data["UspsZip"]
        )
    if "UspsZipPlus4" in data:
        import aws_sdk_geo_places.types.usps_zip_plus4

        out["usps_zip_plus4"] = (
            aws_sdk_geo_places.types.usps_zip_plus4.deserialize_json(
                data["UspsZipPlus4"]
            )
        )
    return out
