"""Generated from Smithy shape ``com.amazonaws.appstream#DomainJoinInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.directory_name
    import aws_sdk_appstream.types.organizational_unit_distinguished_name


class DomainJoinInfo(TypedDict):
    directory_name: NotRequired["aws_sdk_appstream.types.directory_name.DirectoryName"]
    """<p>The fully qualified name of the directory (for example, corp.example.com).</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "aws_sdk_appstream.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>The distinguished name of the organizational unit for computer accounts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainJoinInfo) -> dict:
    out: dict = {}
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainJoinInfo:
    out: DomainJoinInfo = {}  # type: ignore[typeddict-item]
    if "DirectoryName" in data:
        out["directory_name"] = data["DirectoryName"]
    if "OrganizationalUnitDistinguishedName" in data:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    return out
