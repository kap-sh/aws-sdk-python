"""Generated from Smithy shape ``com.amazonaws.route53domains#SortCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.list_domains_attribute_name
    import aws_sdk_route_53_domains.types.sort_order


class SortCondition(TypedDict):
    name: "aws_sdk_route_53_domains.types.list_domains_attribute_name.ListDomainsAttributeName"
    """<p>Field to be used for sorting the list of domains. It can be either the name or the expiration for a domain. Note that if <code>filterCondition</code> is used in the same <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains__ListDomains.html\">ListDomains</a> call, the field used for sorting has to be the same as the field used for filtering.</p>"""
    sort_order: "aws_sdk_route_53_domains.types.sort_order.SortOrder"
    """<p>The sort order for a list of domains. Either ascending (ASC) or descending (DES).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortCondition) -> dict:
    out: dict = {}
    import aws_sdk_route_53_domains.types.list_domains_attribute_name

    out["Name"] = (
        aws_sdk_route_53_domains.types.list_domains_attribute_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_route_53_domains.types.sort_order

    out["SortOrder"] = aws_sdk_route_53_domains.types.sort_order.serialize_aws_json_1_1(
        value["sort_order"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SortCondition:
    out: SortCondition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_route_53_domains.types.list_domains_attribute_name

        out["name"] = (
            aws_sdk_route_53_domains.types.list_domains_attribute_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("SortCondition.name required")
    if "SortOrder" in data:
        import aws_sdk_route_53_domains.types.sort_order

        out["sort_order"] = (
            aws_sdk_route_53_domains.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    else:
        raise DeserializationError("SortCondition.sort_order required")
    return out
