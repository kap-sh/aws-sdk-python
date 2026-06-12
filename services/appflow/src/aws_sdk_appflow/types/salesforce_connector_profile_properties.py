"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceConnectorProfileProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.instance_url


class SalesforceConnectorProfileProperties(TypedDict):
    instance_url: NotRequired["aws_sdk_appflow.types.instance_url.InstanceUrl"]
    """<p> The location of the Salesforce resource. </p>"""
    is_sandbox_environment: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Indicates whether the connector profile applies to a sandbox or production environment. </p>"""
    use_private_link_for_metadata_and_authorization: (
        "aws_sdk_appflow.types.boolean.Boolean"
    )
    """<p>If the connection mode for the connector profile is private, this parameter sets whether Amazon AppFlow uses the private network to send metadata and authorization calls to Salesforce. Amazon AppFlow sends private calls through Amazon Web Services PrivateLink. These calls travel through Amazon Web Services infrastructure without being exposed to the public internet.</p> <p>Set either of the following values:</p> <dl> <dt>true</dt> <dd> <p>Amazon AppFlow sends all calls to Salesforce over the private network.</p> <p>These private calls are:</p> <ul> <li> <p>Calls to get metadata about your Salesforce records. This metadata describes your Salesforce objects and their fields.</p> </li> <li> <p>Calls to get or refresh access tokens that allow Amazon AppFlow to access your Salesforce records.</p> </li> <li> <p>Calls to transfer your Salesforce records as part of a flow run.</p> </li> </ul> </dd> <dt>false</dt> <dd> <p>The default value. Amazon AppFlow sends some calls to Salesforce privately and other calls over the public internet.</p> <p>The public calls are: </p> <ul> <li> <p>Calls to get metadata about your Salesforce records.</p> </li> <li> <p>Calls to get or refresh access tokens.</p> </li> </ul> <p>The private calls are:</p> <ul> <li> <p>Calls to transfer your Salesforce records as part of a flow run.</p> </li> </ul> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceConnectorProfileProperties) -> dict:
    out: dict = {}
    if "instance_url" in value:
        out["instanceUrl"] = value["instance_url"]
    out["isSandboxEnvironment"] = value.get("is_sandbox_environment", False)
    out["usePrivateLinkForMetadataAndAuthorization"] = value.get(
        "use_private_link_for_metadata_and_authorization", False
    )
    return out


def deserialize_json(data: dict) -> SalesforceConnectorProfileProperties:
    out: SalesforceConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    if "isSandboxEnvironment" in data:
        out["is_sandbox_environment"] = data["isSandboxEnvironment"]
    else:
        out["is_sandbox_environment"] = False
    if "usePrivateLinkForMetadataAndAuthorization" in data:
        out["use_private_link_for_metadata_and_authorization"] = data[
            "usePrivateLinkForMetadataAndAuthorization"
        ]
    else:
        out["use_private_link_for_metadata_and_authorization"] = False
    return out
