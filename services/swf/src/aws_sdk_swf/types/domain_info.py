"""Generated from Smithy shape ``com.amazonaws.swf#DomainInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.arn
    import aws_sdk_swf.types.description
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.registration_status


class DomainInfo(TypedDict, closed=True):
    name: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain. This name is unique within the account.</p>"""
    status: "aws_sdk_swf.types.registration_status.RegistrationStatus"
    """<p>The status of the domain:</p> <ul> <li> <p> <code>REGISTERED</code> – The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions. </p> </li> <li> <p> <code>DEPRECATED</code> – The domain was deprecated using <a>DeprecateDomain</a>, but is still in use. You should not create new workflow executions in this domain. </p> </li> </ul>"""
    description: NotRequired["aws_sdk_swf.types.description.Description"]
    """<p>The description of the domain provided through <a>RegisterDomain</a>.</p>"""
    arn: NotRequired["aws_sdk_swf.types.arn.Arn"]
    """<p>The ARN of the domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainInfo) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_swf.types.registration_status

    out["status"] = aws_sdk_swf.types.registration_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainInfo:
    out: DomainInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DomainInfo.name required")
    if "status" in data:
        import aws_sdk_swf.types.registration_status

        out["status"] = aws_sdk_swf.types.registration_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("DomainInfo.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
