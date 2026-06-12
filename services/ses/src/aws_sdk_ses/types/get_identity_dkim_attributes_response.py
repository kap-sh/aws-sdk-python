"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityDkimAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.dkim_attributes


class GetIdentityDkimAttributesResponse(TypedDict):
    dkim_attributes: "aws_sdk_ses.types.dkim_attributes.DkimAttributes"
    """<p>The DKIM attributes for an email address or a domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityDkimAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.dkim_attributes

    aws_sdk_ses.types.dkim_attributes.serialize_query(
        value["dkim_attributes"], pairs, f"{prefix}.DkimAttributes"
    )


def deserialize_query(el: Element) -> GetIdentityDkimAttributesResponse:
    out: GetIdentityDkimAttributesResponse = {}  # type: ignore[typeddict-item]
    child_dkim_attributes = el.find("DkimAttributes")
    if child_dkim_attributes is not None:
        import aws_sdk_ses.types.dkim_attributes

        out["dkim_attributes"] = aws_sdk_ses.types.dkim_attributes.deserialize_query(
            child_dkim_attributes
        )
    else:
        raise DeserializationError(
            "GetIdentityDkimAttributesResponse.dkim_attributes required"
        )
    return out
