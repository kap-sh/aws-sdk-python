"""Generated from Smithy shape ``com.amazonaws.fsx#Alias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.alias_lifecycle
    import aws_sdk_fsx.types.alternate_dns_name


class Alias(TypedDict):
    name: NotRequired["aws_sdk_fsx.types.alternate_dns_name.AlternateDNSName"]
    """<p>The name of the DNS alias. The alias name has to meet the following requirements:</p> <ul> <li> <p>Formatted as a fully-qualified domain name (FQDN), <code>hostname.domain</code>, for example, <code>accounting.example.com</code>.</p> </li> <li> <p>Can contain alphanumeric characters, the underscore (_), and the hyphen (-).</p> </li> <li> <p>Cannot start or end with a hyphen.</p> </li> <li> <p>Can start with a numeric.</p> </li> </ul> <p>For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.</p>"""
    lifecycle: NotRequired["aws_sdk_fsx.types.alias_lifecycle.AliasLifecycle"]
    """<p>Describes the state of the DNS alias.</p> <ul> <li> <p>AVAILABLE - The DNS alias is associated with an Amazon FSx file system.</p> </li> <li> <p>CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.</p> </li> <li> <p>CREATE_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.</p> </li> <li> <p>DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.</p> </li> <li> <p>DELETE_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alias) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.alias_lifecycle

        out["Lifecycle"] = aws_sdk_fsx.types.alias_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Alias:
    out: Alias = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.alias_lifecycle

        out["lifecycle"] = aws_sdk_fsx.types.alias_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    return out
