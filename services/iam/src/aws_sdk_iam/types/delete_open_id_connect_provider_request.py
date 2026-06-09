"""Generated from Smithy shape ``com.amazonaws.iam#DeleteOpenIDConnectProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type


class DeleteOpenIDConnectProviderRequest(TypedDict):
    open_id_connect_provider_arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenID Connect provider resource ARNs by using the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html\">ListOpenIDConnectProviders</a> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteOpenIDConnectProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (
            f"{prefix}.OpenIDConnectProviderArn",
            str(value["open_id_connect_provider_arn"]),
        )
    )


def deserialize_query(el: Element) -> DeleteOpenIDConnectProviderRequest:
    out: DeleteOpenIDConnectProviderRequest = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    else:
        raise DeserializationError(
            "DeleteOpenIDConnectProviderRequest.open_id_connect_provider_arn required"
        )
    return out
