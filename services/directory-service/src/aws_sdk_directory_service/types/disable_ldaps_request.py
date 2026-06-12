"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableLDAPSRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.ldaps_type


class DisableLDAPSRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    type: "aws_sdk_directory_service.types.ldaps_type.LDAPSType"
    """<p>The type of LDAP security to enable. Currently only the value <code>Client</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableLDAPSRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_directory_service.types.ldaps_type

    out["Type"] = aws_sdk_directory_service.types.ldaps_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableLDAPSRequest:
    out: DisableLDAPSRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DisableLDAPSRequest.directory_id required")
    if "Type" in data:
        import aws_sdk_directory_service.types.ldaps_type

        out["type"] = (
            aws_sdk_directory_service.types.ldaps_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("DisableLDAPSRequest.type required")
    return out
