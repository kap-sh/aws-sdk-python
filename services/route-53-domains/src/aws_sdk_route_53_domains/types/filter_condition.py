"""Generated from Smithy shape ``com.amazonaws.route53domains#FilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.list_domains_attribute_name
    import aws_sdk_route_53_domains.types.operator
    import aws_sdk_route_53_domains.types.values


class FilterCondition(TypedDict):
    name: "aws_sdk_route_53_domains.types.list_domains_attribute_name.ListDomainsAttributeName"
    """<p>Name of the field which should be used for filtering the list of domains.</p>"""
    operator: "aws_sdk_route_53_domains.types.operator.Operator"
    """<p>The operator values for filtering domain names. The values can be:</p> <ul> <li> <p> <code>LE</code>: Less than, or equal to</p> </li> <li> <p> <code>GE</code>: Greater than, or equal to</p> </li> <li> <p> <code>BEGINS_WITH</code>: Begins with</p> </li> </ul>"""
    values: "aws_sdk_route_53_domains.types.values.Values"
    """<p> An array of strings presenting values to compare. Only 1 item in the list is currently supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterCondition) -> dict:
    out: dict = {}
    import aws_sdk_route_53_domains.types.list_domains_attribute_name

    out["Name"] = (
        aws_sdk_route_53_domains.types.list_domains_attribute_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_route_53_domains.types.operator

    out["Operator"] = aws_sdk_route_53_domains.types.operator.serialize_aws_json_1_1(
        value["operator"]
    )
    import aws_sdk_route_53_domains.types.values

    out["Values"] = aws_sdk_route_53_domains.types.values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterCondition:
    out: FilterCondition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_route_53_domains.types.list_domains_attribute_name

        out["name"] = (
            aws_sdk_route_53_domains.types.list_domains_attribute_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("FilterCondition.name required")
    if "Operator" in data:
        import aws_sdk_route_53_domains.types.operator

        out["operator"] = (
            aws_sdk_route_53_domains.types.operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("FilterCondition.operator required")
    if "Values" in data:
        import aws_sdk_route_53_domains.types.values

        out["values"] = aws_sdk_route_53_domains.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("FilterCondition.values required")
    return out
