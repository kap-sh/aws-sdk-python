"""Generated from Smithy shape ``com.amazonaws.rds#Option``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.db_security_group_membership_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.option_setting_configuration_list
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.vpc_security_group_membership_list


class Option(TypedDict):
    option_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the option.</p>"""
    option_description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The description of the option.</p>"""
    persistent: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether this option is persistent.</p>"""
    permanent: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether this option is permanent.</p>"""
    port: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>If required, the port configured for this option to use.</p>"""
    option_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The version of the option.</p>"""
    option_settings: NotRequired[
        "aws_sdk_rds.types.option_setting_configuration_list.OptionSettingConfigurationList"
    ]
    """<p>The option settings for this option.</p>"""
    db_security_group_memberships: NotRequired[
        "aws_sdk_rds.types.db_security_group_membership_list.DBSecurityGroupMembershipList"
    ]
    """<p>If the option requires access to a port, then this DB security group allows access to the port.</p>"""
    vpc_security_group_memberships: NotRequired[
        "aws_sdk_rds.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>If the option requires access to a port, then this VPC security group allows access to the port.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Option, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "option_name" in value:
        pairs.append((f"{prefix}.OptionName", str(value["option_name"])))
    if "option_description" in value:
        pairs.append((f"{prefix}.OptionDescription", str(value["option_description"])))
    if "persistent" in value:
        pairs.append(
            (f"{prefix}.Persistent", "true" if value["persistent"] else "false")
        )
    if "permanent" in value:
        pairs.append((f"{prefix}.Permanent", "true" if value["permanent"] else "false"))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "option_version" in value:
        pairs.append((f"{prefix}.OptionVersion", str(value["option_version"])))
    if "option_settings" in value:
        import aws_sdk_rds.types.option_setting_configuration_list

        aws_sdk_rds.types.option_setting_configuration_list.serialize_query(
            value["option_settings"], pairs, f"{prefix}.OptionSettings"
        )
    if "db_security_group_memberships" in value:
        import aws_sdk_rds.types.db_security_group_membership_list

        aws_sdk_rds.types.db_security_group_membership_list.serialize_query(
            value["db_security_group_memberships"],
            pairs,
            f"{prefix}.DBSecurityGroupMemberships",
        )
    if "vpc_security_group_memberships" in value:
        import aws_sdk_rds.types.vpc_security_group_membership_list

        aws_sdk_rds.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_group_memberships"],
            pairs,
            f"{prefix}.VpcSecurityGroupMemberships",
        )


def deserialize_query(el: Element) -> Option:
    out: Option = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_option_description = el.find("OptionDescription")
    if child_option_description is not None:
        out["option_description"] = str(child_option_description.text or "")
    child_persistent = el.find("Persistent")
    if child_persistent is not None:
        out["persistent"] = (child_persistent.text or "").lower() == "true"
    child_permanent = el.find("Permanent")
    if child_permanent is not None:
        out["permanent"] = (child_permanent.text or "").lower() == "true"
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_option_version = el.find("OptionVersion")
    if child_option_version is not None:
        out["option_version"] = str(child_option_version.text or "")
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import aws_sdk_rds.types.option_setting_configuration_list

        out["option_settings"] = (
            aws_sdk_rds.types.option_setting_configuration_list.deserialize_query(
                child_option_settings
            )
        )
    child_db_security_group_memberships = el.find("DBSecurityGroupMemberships")
    if child_db_security_group_memberships is not None:
        import aws_sdk_rds.types.db_security_group_membership_list

        out["db_security_group_memberships"] = (
            aws_sdk_rds.types.db_security_group_membership_list.deserialize_query(
                child_db_security_group_memberships
            )
        )
    child_vpc_security_group_memberships = el.find("VpcSecurityGroupMemberships")
    if child_vpc_security_group_memberships is not None:
        import aws_sdk_rds.types.vpc_security_group_membership_list

        out["vpc_security_group_memberships"] = (
            aws_sdk_rds.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_group_memberships
            )
        )
    return out
