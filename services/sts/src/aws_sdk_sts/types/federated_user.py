"""Generated from Smithy shape ``com.amazonaws.sts#FederatedUser``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sts.types.arn_type
    import aws_sdk_sts.types.federated_id_type


class FederatedUser(TypedDict):
    federated_user_id: "aws_sdk_sts.types.federated_id_type.federatedIdType"
    """<p>The string that identifies the federated user associated with the credentials, similar to the unique ID of an IAM user.</p>"""
    arn: "aws_sdk_sts.types.arn_type.arnType"
    r"""<p>The ARN that specifies the federated user that is associated with the credentials. For more information about ARNs and how to use them in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FederatedUser, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.FederatedUserId", str(value["federated_user_id"])))
    pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_query(el: Element) -> FederatedUser:
    out: FederatedUser = {}  # type: ignore[typeddict-item]
    child_federated_user_id = el.find("FederatedUserId")
    if child_federated_user_id is not None:
        out["federated_user_id"] = str(child_federated_user_id.text or "")
    else:
        raise DeserializationError("FederatedUser.federated_user_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("FederatedUser.arn required")
    return out
