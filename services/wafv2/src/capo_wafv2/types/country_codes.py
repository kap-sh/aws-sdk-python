"""Generated from Smithy shape ``com.amazonaws.wafv2#CountryCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.country_code

CountryCodes: TypeAlias = list["capo_wafv2.types.country_code.CountryCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CountryCodes) -> list:
    import capo_wafv2.types.country_code

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.country_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CountryCodes:
    import capo_wafv2.types.country_code

    out: CountryCodes = []
    for item in data:
        out.append(capo_wafv2.types.country_code.deserialize_aws_json_1_1(item))
    return out
