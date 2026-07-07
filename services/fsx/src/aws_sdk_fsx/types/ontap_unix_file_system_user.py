"""Generated from Smithy shape ``com.amazonaws.fsx#OntapUnixFileSystemUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.ontap_file_system_user_name


class OntapUnixFileSystemUser(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_fsx.types.ontap_file_system_user_name.OntapFileSystemUserName"
    ]
    """<p>The name of the UNIX user. The name can be up to 256 characters long.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapUnixFileSystemUser) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OntapUnixFileSystemUser:
    out: OntapUnixFileSystemUser = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
