"""Generated from Smithy shape ``com.amazonaws.wafregional#AssociateWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_arn
    import aws_sdk_waf_regional.types.resource_id


class AssociateWebACLRequest(TypedDict, closed=True):
    web_acl_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier (ID) for the web ACL. </p>"""
    resource_arn: "aws_sdk_waf_regional.types.resource_arn.ResourceArn"
    """<p>The ARN (Amazon Resource Name) of the resource to be protected, either an application load balancer or Amazon API Gateway stage. </p> <p>The ARN should be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway stage: <code>arn:aws:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWebACLRequest:
    out: AssociateWebACLRequest = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("AssociateWebACLRequest.web_acl_id required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("AssociateWebACLRequest.resource_arn required")
    return out
