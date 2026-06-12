"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeInstancesHealthRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_id
    import aws_sdk_elastic_beanstalk.types.environment_name
    import aws_sdk_elastic_beanstalk.types.instances_health_attributes
    import aws_sdk_elastic_beanstalk.types.next_token


class DescribeInstancesHealthRequest(TypedDict):
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>Specify the AWS Elastic Beanstalk environment by name.</p>"""
    environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>Specify the AWS Elastic Beanstalk environment by ID.</p>"""
    attribute_names: NotRequired[
        "aws_sdk_elastic_beanstalk.types.instances_health_attributes.InstancesHealthAttributes"
    ]
    """<p>Specifies the response elements you wish to receive. To retrieve all attributes, set to <code>All</code>. If no attribute names are specified, returns a list of instances.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.next_token.NextToken"]
    """<p>Specify the pagination token returned by a previous call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInstancesHealthRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "attribute_names" in value:
        import aws_sdk_elastic_beanstalk.types.instances_health_attributes

        aws_sdk_elastic_beanstalk.types.instances_health_attributes.serialize_query(
            value["attribute_names"], pairs, f"{prefix}.AttributeNames"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeInstancesHealthRequest:
    out: DescribeInstancesHealthRequest = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_attribute_names = el.find("AttributeNames")
    if child_attribute_names is not None:
        import aws_sdk_elastic_beanstalk.types.instances_health_attributes

        out["attribute_names"] = (
            aws_sdk_elastic_beanstalk.types.instances_health_attributes.deserialize_query(
                child_attribute_names
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
