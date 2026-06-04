"""Generated from Smithy shape ``com.amazonaws.iam#AccessKey``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.access_key_id_type
    import aws_sdk_iam.types.access_key_secret_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.status_type
    import aws_sdk_iam.types.user_name_type


class AccessKey(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user that the access key is associated with.</p>"""
    access_key_id: "aws_sdk_iam.types.access_key_id_type.accessKeyIdType"
    """<p>The ID for this access key.</p>"""
    status: "aws_sdk_iam.types.status_type.statusType"
    """<p>The status of the access key. <code>Active</code> means that the key is valid for API calls, while <code>Inactive</code> means it is not. </p>"""
    secret_access_key: "aws_sdk_iam.types.access_key_secret_type.accessKeySecretType"
    """<p>The secret key used to sign requests.</p>"""
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date when the access key was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessKey, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.AccessKeyId", str(value["access_key_id"])))
    import aws_sdk_iam.types.status_type

    aws_sdk_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )
    pairs.append((f"{prefix}.SecretAccessKey", str(value["secret_access_key"])))
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )


def deserialize_query(el: Element) -> AccessKey:
    out: AccessKey = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("AccessKey.user_name required")
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        raise DeserializationError("AccessKey.access_key_id required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_iam.types.status_type

        out["status"] = aws_sdk_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("AccessKey.status required")
    child_secret_access_key = el.find("SecretAccessKey")
    if child_secret_access_key is not None:
        out["secret_access_key"] = str(child_secret_access_key.text or "")
    else:
        raise DeserializationError("AccessKey.secret_access_key required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    return out
