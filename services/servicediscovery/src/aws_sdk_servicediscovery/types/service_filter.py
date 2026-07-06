"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.filter_condition
    import aws_sdk_servicediscovery.types.filter_values
    import aws_sdk_servicediscovery.types.service_filter_name


class ServiceFilter(TypedDict, closed=True):
    name: "aws_sdk_servicediscovery.types.service_filter_name.ServiceFilterName"
    r"""<p>Specify the services that you want to get using one of the following.</p> <ul> <li> <p> <code>NAMESPACE_ID</code>: Gets the services associated with the specified namespace.</p> </li> <li> <p> <code>RESOURCE_OWNER</code>: Gets the services associated with the namespaces created by your Amazon Web Services account or by other accounts. This can be used to filter for services created in a shared namespace. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p> </li> </ul>"""
    values: "aws_sdk_servicediscovery.types.filter_values.FilterValues"
    """<p>The values that are applicable to the value that you specify for <code>Condition</code> to filter the list of services.</p> <ul> <li> <p> <b>NAMESPACE_ID</b>: Specify one namespace ID or ARN. Specify the namespace ARN for namespaces that are shared with your Amazon Web Services account.</p> </li> <li> <p> <b>RESOURCE_OWNER</b>: Specify one of <code>SELF</code> or <code>OTHER_ACCOUNTS</code>. <code>SELF</code> can be used to filter services associated with namespaces created by you and <code>OTHER_ACCOUNTS</code> can be used to filter services associated with namespaces that were shared with you.</p> </li> </ul>"""
    condition: NotRequired[
        "aws_sdk_servicediscovery.types.filter_condition.FilterCondition"
    ]
    """<p>The operator that you want to use to determine whether a service is returned by <code>ListServices</code>. Valid values for <code>Condition</code> include the following:</p> <ul> <li> <p> <code>EQ</code>: When you specify <code>EQ</code>, specify one value. <code>EQ</code> is the default condition and can be omitted.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceFilter) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.service_filter_name

    out["Name"] = (
        aws_sdk_servicediscovery.types.service_filter_name.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> ServiceFilter:
    out: ServiceFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_servicediscovery.types.service_filter_name

        out["name"] = (
            aws_sdk_servicediscovery.types.service_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("ServiceFilter.name required")
    if "Values" in data:
        import aws_sdk_servicediscovery.types.filter_values

        out["values"] = (
            aws_sdk_servicediscovery.types.filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ServiceFilter.values required")
    if "Condition" in data:
        import aws_sdk_servicediscovery.types.filter_condition

        out["condition"] = (
            aws_sdk_servicediscovery.types.filter_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    return out
