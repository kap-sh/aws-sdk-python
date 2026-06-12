"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.filter_condition
    import aws_sdk_servicediscovery.types.filter_values
    import aws_sdk_servicediscovery.types.namespace_filter_name


class NamespaceFilter(TypedDict):
    name: "aws_sdk_servicediscovery.types.namespace_filter_name.NamespaceFilterName"
    """<p>Specify the namespaces that you want to get using one of the following.</p> <ul> <li> <p> <code>TYPE</code>: Gets the namespaces of the specified type.</p> </li> <li> <p> <code>NAME</code>: Gets the namespaces with the specified name.</p> </li> <li> <p> <code>HTTP_NAME</code>: Gets the namespaces with the specified HTTP name.</p> </li> <li> <p> <code>RESOURCE_OWNER</code>: Gets the namespaces created by your Amazon Web Services account or by other accounts. This can be used to filter for shared namespaces. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p> </li> </ul>"""
    values: "aws_sdk_servicediscovery.types.filter_values.FilterValues"
    """<p>Specify the values that are applicable to the value that you specify for <code>Name</code>.</p> <ul> <li> <p> <code>TYPE</code>: Specify <code>HTTP</code>, <code>DNS_PUBLIC</code>, or <code>DNS_PRIVATE</code>.</p> </li> <li> <p> <code>NAME</code>: Specify the name of the namespace, which is found in <code>Namespace.Name</code>.</p> </li> <li> <p> <code>HTTP_NAME</code>: Specify the HTTP name of the namespace, which is found in <code>Namespace.Properties.HttpProperties.HttpName</code>.</p> </li> <li> <p> <code>RESOURCE_OWNER</code>: Specify one of <code>SELF</code> or <code>OTHER_ACCOUNTS</code>. <code>SELF</code> can be used to filter namespaces created by you and <code>OTHER_ACCOUNTS</code> can be used to filter namespaces shared with you that were created by other accounts.</p> </li> </ul>"""
    condition: NotRequired[
        "aws_sdk_servicediscovery.types.filter_condition.FilterCondition"
    ]
    """<p>Specify the operator that you want to use to determine whether a namespace matches the specified value. Valid values for <code>Condition</code> are one of the following.</p> <ul> <li> <p> <code>EQ</code>: When you specify <code>EQ</code> for <code>Condition</code>, you can specify only one value. <code>EQ</code> is supported for <code>TYPE</code>, <code>NAME</code>, <code>RESOURCE_OWNER</code> and <code>HTTP_NAME</code>. <code>EQ</code> is the default condition and can be omitted.</p> </li> <li> <p> <code>BEGINS_WITH</code>: When you specify <code>BEGINS_WITH</code> for <code>Condition</code>, you can specify only one value. <code>BEGINS_WITH</code> is supported for <code>TYPE</code>, <code>NAME</code>, and <code>HTTP_NAME</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceFilter) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.namespace_filter_name

    out["Name"] = (
        aws_sdk_servicediscovery.types.namespace_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_servicediscovery.types.filter_values

    out["Values"] = aws_sdk_servicediscovery.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    if "condition" in value:
        import aws_sdk_servicediscovery.types.filter_condition

        out["Condition"] = (
            aws_sdk_servicediscovery.types.filter_condition.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceFilter:
    out: NamespaceFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_servicediscovery.types.namespace_filter_name

        out["name"] = (
            aws_sdk_servicediscovery.types.namespace_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("NamespaceFilter.name required")
    if "Values" in data:
        import aws_sdk_servicediscovery.types.filter_values

        out["values"] = (
            aws_sdk_servicediscovery.types.filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("NamespaceFilter.values required")
    if "Condition" in data:
        import aws_sdk_servicediscovery.types.filter_condition

        out["condition"] = (
            aws_sdk_servicediscovery.types.filter_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    return out
