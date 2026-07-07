"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.default_registry_alias_flag
    import aws_sdk_ecr_public.types.primary_registry_alias_flag
    import aws_sdk_ecr_public.types.registry_alias_name
    import aws_sdk_ecr_public.types.registry_alias_status


class RegistryAlias(TypedDict, closed=True):
    name: "aws_sdk_ecr_public.types.registry_alias_name.RegistryAliasName"
    """<p>The name of the registry alias.</p>"""
    status: "aws_sdk_ecr_public.types.registry_alias_status.RegistryAliasStatus"
    """<p>The status of the registry alias.</p>"""
    primary_registry_alias: (
        "aws_sdk_ecr_public.types.primary_registry_alias_flag.PrimaryRegistryAliasFlag"
    )
    """<p>Indicates whether the registry alias is the primary alias for the registry. If true, the alias is the primary registry alias and is displayed in both the repository URL and the image URI used in the <code>docker pull</code> commands on the Amazon ECR Public Gallery.</p> <note> <p>A registry alias that isn't the primary registry alias can be used in the repository URI in a <code>docker pull</code> command.</p> </note>"""
    default_registry_alias: (
        "aws_sdk_ecr_public.types.default_registry_alias_flag.DefaultRegistryAliasFlag"
    )
    """<p>Indicates whether the registry alias is the default alias for the registry. When the first public repository is created, your public registry is assigned a default registry alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryAlias) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_ecr_public.types.registry_alias_status

    out["status"] = (
        aws_sdk_ecr_public.types.registry_alias_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    out["primaryRegistryAlias"] = value.get("primary_registry_alias", False)
    out["defaultRegistryAlias"] = value.get("default_registry_alias", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryAlias:
    out: RegistryAlias = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegistryAlias.name required")
    if "status" in data:
        import aws_sdk_ecr_public.types.registry_alias_status

        out["status"] = (
            aws_sdk_ecr_public.types.registry_alias_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RegistryAlias.status required")
    if "primaryRegistryAlias" in data:
        out["primary_registry_alias"] = data["primaryRegistryAlias"]
    else:
        out["primary_registry_alias"] = False
    if "defaultRegistryAlias" in data:
        out["default_registry_alias"] = data["defaultRegistryAlias"]
    else:
        out["default_registry_alias"] = False
    return out
