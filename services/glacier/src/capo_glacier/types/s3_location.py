"""Generated from Smithy shape ``com.amazonaws.glacier#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.access_control_policy_list
    import capo_glacier.types.canned_acl
    import capo_glacier.types.encryption
    import capo_glacier.types.hashmap
    import capo_glacier.types.storage_class
    import capo_glacier.types.string


class S3Location(TypedDict, closed=True):
    bucket_name: NotRequired["capo_glacier.types.string.string"]
    """<p>The name of the Amazon S3 bucket where the job results are stored.</p>"""
    prefix: NotRequired["capo_glacier.types.string.string"]
    """<p>The prefix that is prepended to the results for this request.</p>"""
    encryption: NotRequired["capo_glacier.types.encryption.Encryption"]
    """<p>Contains information about the encryption used to store the job results in Amazon S3.</p>"""
    canned_acl: NotRequired["capo_glacier.types.canned_acl.CannedACL"]
    """<p>The canned access control list (ACL) to apply to the job results.</p>"""
    access_control_list: NotRequired[
        "capo_glacier.types.access_control_policy_list.AccessControlPolicyList"
    ]
    """<p>A list of grants that control access to the staged results.</p>"""
    tagging: NotRequired["capo_glacier.types.hashmap.hashmap"]
    """<p>The tag-set that is applied to the job results.</p>"""
    user_metadata: NotRequired["capo_glacier.types.hashmap.hashmap"]
    """<p>A map of metadata to store with the job results in Amazon S3.</p>"""
    storage_class: NotRequired["capo_glacier.types.storage_class.StorageClass"]
    """<p>The storage class used to store the job results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "encryption" in value:
        import capo_glacier.types.encryption

        out["Encryption"] = capo_glacier.types.encryption.serialize_json(
            value["encryption"]
        )
    if "canned_acl" in value:
        import capo_glacier.types.canned_acl

        out["CannedACL"] = capo_glacier.types.canned_acl.serialize_json(
            value["canned_acl"]
        )
    if "access_control_list" in value:
        import capo_glacier.types.access_control_policy_list

        out["AccessControlList"] = (
            capo_glacier.types.access_control_policy_list.serialize_json(
                value["access_control_list"]
            )
        )
    if "tagging" in value:
        import capo_glacier.types.hashmap

        out["Tagging"] = capo_glacier.types.hashmap.serialize_json(value["tagging"])
    if "user_metadata" in value:
        import capo_glacier.types.hashmap

        out["UserMetadata"] = capo_glacier.types.hashmap.serialize_json(
            value["user_metadata"]
        )
    if "storage_class" in value:
        import capo_glacier.types.storage_class

        out["StorageClass"] = capo_glacier.types.storage_class.serialize_json(
            value["storage_class"]
        )
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Encryption" in data:
        import capo_glacier.types.encryption

        out["encryption"] = capo_glacier.types.encryption.deserialize_json(
            data["Encryption"]
        )
    if "CannedACL" in data:
        import capo_glacier.types.canned_acl

        out["canned_acl"] = capo_glacier.types.canned_acl.deserialize_json(
            data["CannedACL"]
        )
    if "AccessControlList" in data:
        import capo_glacier.types.access_control_policy_list

        out["access_control_list"] = (
            capo_glacier.types.access_control_policy_list.deserialize_json(
                data["AccessControlList"]
            )
        )
    if "Tagging" in data:
        import capo_glacier.types.hashmap

        out["tagging"] = capo_glacier.types.hashmap.deserialize_json(data["Tagging"])
    if "UserMetadata" in data:
        import capo_glacier.types.hashmap

        out["user_metadata"] = capo_glacier.types.hashmap.deserialize_json(
            data["UserMetadata"]
        )
    if "StorageClass" in data:
        import capo_glacier.types.storage_class

        out["storage_class"] = capo_glacier.types.storage_class.deserialize_json(
            data["StorageClass"]
        )
    return out
