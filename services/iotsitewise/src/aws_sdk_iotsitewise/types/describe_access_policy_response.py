"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.identity
    import aws_sdk_iotsitewise.types.permission
    import aws_sdk_iotsitewise.types.resource
    import aws_sdk_iotsitewise.types.timestamp


class DescribeAccessPolicyResponse(TypedDict, closed=True):
    access_policy_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    access_policy_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the access policy, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}</code> </p>"""
    access_policy_identity: "aws_sdk_iotsitewise.types.identity.Identity"
    """<p>The identity (IAM Identity Center user, IAM Identity Center group, or IAM user) to which this access policy applies.</p>"""
    access_policy_resource: "aws_sdk_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource (portal or project) to which this access policy provides access.</p>"""
    access_policy_permission: "aws_sdk_iotsitewise.types.permission.Permission"
    """<p>The access policy permission. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    access_policy_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the access policy was created, in Unix epoch time.</p>"""
    access_policy_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the access policy was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPolicyResponse) -> dict:
    out: dict = {}
    out["accessPolicyId"] = value["access_policy_id"]
    out["accessPolicyArn"] = value["access_policy_arn"]
    import aws_sdk_iotsitewise.types.identity

    out["accessPolicyIdentity"] = aws_sdk_iotsitewise.types.identity.serialize_json(
        value["access_policy_identity"]
    )
    import aws_sdk_iotsitewise.types.resource

    out["accessPolicyResource"] = aws_sdk_iotsitewise.types.resource.serialize_json(
        value["access_policy_resource"]
    )
    import aws_sdk_iotsitewise.types.permission

    out["accessPolicyPermission"] = aws_sdk_iotsitewise.types.permission.serialize_json(
        value["access_policy_permission"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["accessPolicyCreationDate"] = (
        aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["access_policy_creation_date"]
        )
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["accessPolicyLastUpdateDate"] = (
        aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["access_policy_last_update_date"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeAccessPolicyResponse:
    out: DescribeAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "accessPolicyId" in data:
        out["access_policy_id"] = data["accessPolicyId"]
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_id required"
        )
    if "accessPolicyArn" in data:
        out["access_policy_arn"] = data["accessPolicyArn"]
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_arn required"
        )
    if "accessPolicyIdentity" in data:
        import aws_sdk_iotsitewise.types.identity

        out["access_policy_identity"] = (
            aws_sdk_iotsitewise.types.identity.deserialize_json(
                data["accessPolicyIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_identity required"
        )
    if "accessPolicyResource" in data:
        import aws_sdk_iotsitewise.types.resource

        out["access_policy_resource"] = (
            aws_sdk_iotsitewise.types.resource.deserialize_json(
                data["accessPolicyResource"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_resource required"
        )
    if "accessPolicyPermission" in data:
        import aws_sdk_iotsitewise.types.permission

        out["access_policy_permission"] = (
            aws_sdk_iotsitewise.types.permission.deserialize_json(
                data["accessPolicyPermission"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_permission required"
        )
    if "accessPolicyCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["access_policy_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["accessPolicyCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_creation_date required"
        )
    if "accessPolicyLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["access_policy_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["accessPolicyLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAccessPolicyResponse.access_policy_last_update_date required"
        )
    return out
