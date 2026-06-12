"""Generated from Smithy shape ``com.amazonaws.sts#GetFederationTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.credentials
    import aws_sdk_sts.types.federated_user
    import aws_sdk_sts.types.non_negative_integer_type


class GetFederationTokenResponse(TypedDict):
    credentials: NotRequired["aws_sdk_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    federated_user: NotRequired["aws_sdk_sts.types.federated_user.FederatedUser"]
    """<p>Identifiers for the federated user associated with the credentials (such as <code>arn:aws:sts::123456789012:federated-user/Bob</code> or <code>123456789012:Bob</code>). You can use the federated user's ARN in your resource-based policies, such as an Amazon S3 bucket policy. </p>"""
    packed_policy_size: NotRequired[
        "aws_sdk_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetFederationTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "credentials" in value:
        import aws_sdk_sts.types.credentials

        aws_sdk_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{prefix}.Credentials"
        )
    if "federated_user" in value:
        import aws_sdk_sts.types.federated_user

        aws_sdk_sts.types.federated_user.serialize_query(
            value["federated_user"], pairs, f"{prefix}.FederatedUser"
        )
    if "packed_policy_size" in value:
        pairs.append((f"{prefix}.PackedPolicySize", str(value["packed_policy_size"])))


def deserialize_query(el: Element) -> GetFederationTokenResponse:
    out: GetFederationTokenResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import aws_sdk_sts.types.credentials

        out["credentials"] = aws_sdk_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_federated_user = el.find("FederatedUser")
    if child_federated_user is not None:
        import aws_sdk_sts.types.federated_user

        out["federated_user"] = aws_sdk_sts.types.federated_user.deserialize_query(
            child_federated_user
        )
    child_packed_policy_size = el.find("PackedPolicySize")
    if child_packed_policy_size is not None:
        out["packed_policy_size"] = int(child_packed_policy_size.text or "")
    return out
