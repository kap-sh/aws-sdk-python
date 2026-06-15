"""Generated from Smithy shape ``com.amazonaws.securitylake#UpdateSubscriberRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_identity
    import aws_sdk_securitylake.types.description_string
    import aws_sdk_securitylake.types.log_source_resource_list
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.uuid


class UpdateSubscriberRequest(TypedDict):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>A value created by Security Lake that uniquely identifies your subscription.</p>"""
    subscriber_identity: NotRequired[
        "aws_sdk_securitylake.types.aws_identity.AwsIdentity"
    ]
    """<p>The Amazon Web Services identity used to access your data.</p>"""
    subscriber_name: NotRequired["aws_sdk_securitylake.types.safe_string.SafeString"]
    """<p>The name of the Security Lake account subscriber.</p>"""
    subscriber_description: NotRequired[
        "aws_sdk_securitylake.types.description_string.DescriptionString"
    ]
    """<p>The description of the Security Lake account subscriber.</p>"""
    sources: NotRequired[
        "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
    ]
    r"""<p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html\">Amazon Security Lake User Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriberRequest) -> dict:
    out: dict = {}
    if "subscriber_identity" in value:
        import aws_sdk_securitylake.types.aws_identity

        out["subscriberIdentity"] = (
            aws_sdk_securitylake.types.aws_identity.serialize_json(
                value["subscriber_identity"]
            )
        )
    if "subscriber_name" in value:
        out["subscriberName"] = value["subscriber_name"]
    if "subscriber_description" in value:
        out["subscriberDescription"] = value["subscriber_description"]
    if "sources" in value:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSubscriberRequest:
    out: UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if "subscriberIdentity" in data:
        import aws_sdk_securitylake.types.aws_identity

        out["subscriber_identity"] = (
            aws_sdk_securitylake.types.aws_identity.deserialize_json(
                data["subscriberIdentity"]
            )
        )
    if "subscriberName" in data:
        out["subscriber_name"] = data["subscriberName"]
    if "subscriberDescription" in data:
        out["subscriber_description"] = data["subscriberDescription"]
    if "sources" in data:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    return out
