"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginSslProtocols``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string_list


class AwsCloudFrontDistributionOriginSslProtocols(TypedDict, closed=True):
    items: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list that contains allowed SSL/TLS protocols for this distribution. </p>"""
    quantity: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginSslProtocols) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Items"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["items"]
        )
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginSslProtocols:
    out: AwsCloudFrontDistributionOriginSslProtocols = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_securityhub.types.non_empty_string_list

        out["items"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Items"]
        )
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    return out
