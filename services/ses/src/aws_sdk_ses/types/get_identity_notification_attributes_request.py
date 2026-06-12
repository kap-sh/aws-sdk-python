"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityNotificationAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity_list


class GetIdentityNotificationAttributesRequest(TypedDict):
    identities: "aws_sdk_ses.types.identity_list.IdentityList"
    """<p>A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityNotificationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.identity_list

    aws_sdk_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{prefix}.Identities"
    )


def deserialize_query(el: Element) -> GetIdentityNotificationAttributesRequest:
    out: GetIdentityNotificationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import aws_sdk_ses.types.identity_list

        out["identities"] = aws_sdk_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        raise DeserializationError(
            "GetIdentityNotificationAttributesRequest.identities required"
        )
    return out
