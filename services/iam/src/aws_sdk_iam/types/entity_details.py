"""Generated from Smithy shape ``com.amazonaws.iam#EntityDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.entity_info


class EntityDetails(TypedDict):
    entity_info: "aws_sdk_iam.types.entity_info.EntityInfo"
    """<p>The <code>EntityInfo</code> object that contains details about the entity (user or role).</p>"""
    last_authenticated: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the authenticated entity last attempted to access Amazon Web Services. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period\">tracking period</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.entity_info

    aws_sdk_iam.types.entity_info.serialize_query(
        value["entity_info"], pairs, f"{prefix}.EntityInfo"
    )
    if "last_authenticated" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["last_authenticated"], pairs, f"{prefix}.LastAuthenticated"
        )


def deserialize_query(el: Element) -> EntityDetails:
    out: EntityDetails = {}  # type: ignore[typeddict-item]
    child_entity_info = el.find("EntityInfo")
    if child_entity_info is not None:
        import aws_sdk_iam.types.entity_info

        out["entity_info"] = aws_sdk_iam.types.entity_info.deserialize_query(
            child_entity_info
        )
    else:
        raise DeserializationError("EntityDetails.entity_info required")
    child_last_authenticated = el.find("LastAuthenticated")
    if child_last_authenticated is not None:
        import aws_sdk_iam.types.date_type

        out["last_authenticated"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_last_authenticated
        )
    return out
