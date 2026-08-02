"""Generated from Smithy shape ``com.amazonaws.iam#AccessKeyMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.access_key_id_type
    import capo_iam.types.date_type
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class AccessKeyMetadata(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The name of the IAM user that the key is associated with.</p>"""
    access_key_id: NotRequired["capo_iam.types.access_key_id_type.accessKeyIdType"]
    """<p>The ID for this access key.</p>"""
    status: NotRequired["capo_iam.types.status_type.statusType"]
    """<p>The status of the access key. <code>Active</code> means that the key is valid for API calls; <code>Inactive</code> means it is not.</p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date when the access key was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessKeyMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "access_key_id" in value:
        pairs.append((f"{key_prefix}AccessKeyId", str(value["access_key_id"])))
    if "status" in value:
        import capo_iam.types.status_type

        capo_iam.types.status_type.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )


def deserialize_query(el: Element) -> AccessKeyMetadata:
    out: AccessKeyMetadata = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    return out
