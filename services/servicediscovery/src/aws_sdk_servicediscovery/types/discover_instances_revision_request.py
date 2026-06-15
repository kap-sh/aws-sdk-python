"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DiscoverInstancesRevisionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.aws_account_id
    import aws_sdk_servicediscovery.types.namespace_name
    import aws_sdk_servicediscovery.types.service_name


class DiscoverInstancesRevisionRequest(TypedDict):
    namespace_name: "aws_sdk_servicediscovery.types.namespace_name.NamespaceName"
    """<p>The <code>HttpName</code> name of the namespace. The <code>HttpName</code> is found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace.</p>"""
    service_name: "aws_sdk_servicediscovery.types.service_name.ServiceName"
    """<p>The name of the service that you specified when you registered the instance.</p>"""
    owner_account: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    r"""<p>The ID of the Amazon Web Services account that owns the namespace associated with the instance, as specified in the namespace <code>ResourceOwner</code> field. For instances associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInstancesRevisionRequest) -> dict:
    out: dict = {}
    out["NamespaceName"] = value["namespace_name"]
    out["ServiceName"] = value["service_name"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInstancesRevisionRequest:
    out: DiscoverInstancesRevisionRequest = {}  # type: ignore[typeddict-item]
    if "NamespaceName" in data:
        out["namespace_name"] = data["NamespaceName"]
    else:
        raise DeserializationError(
            "DiscoverInstancesRevisionRequest.namespace_name required"
        )
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    else:
        raise DeserializationError(
            "DiscoverInstancesRevisionRequest.service_name required"
        )
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    return out
