"""Generated from Smithy shape ``com.amazonaws.rds#OptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_security_group_name_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.option_settings_list
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.vpc_security_group_id_list


class OptionConfiguration(TypedDict, closed=True):
    option_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The configuration of options to include in a group.</p>"""
    port: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The optional port for the option.</p>"""
    option_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The version for the option.</p>"""
    db_security_group_memberships: NotRequired[
        "aws_sdk_rds.types.db_security_group_name_list.DBSecurityGroupNameList"
    ]
    """<p>A list of DB security groups used for this option.</p>"""
    vpc_security_group_memberships: NotRequired[
        "aws_sdk_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group names used for this option.</p>"""
    option_settings: NotRequired[
        "aws_sdk_rds.types.option_settings_list.OptionSettingsList"
    ]
    """<p>The option settings to include in an option group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_name" in value:
        pairs.append((f"{prefix}.OptionName", str(value["option_name"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "option_version" in value:
        pairs.append((f"{prefix}.OptionVersion", str(value["option_version"])))
    if "db_security_group_memberships" in value:
        import aws_sdk_rds.types.db_security_group_name_list

        aws_sdk_rds.types.db_security_group_name_list.serialize_query(
            value["db_security_group_memberships"],
            pairs,
            f"{prefix}.DBSecurityGroupMemberships",
        )
    if "vpc_security_group_memberships" in value:
        import aws_sdk_rds.types.vpc_security_group_id_list

        aws_sdk_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_memberships"],
            pairs,
            f"{prefix}.VpcSecurityGroupMemberships",
        )
    if "option_settings" in value:
        import aws_sdk_rds.types.option_settings_list

        aws_sdk_rds.types.option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{prefix}.OptionSettings"
        )


def deserialize_query(el: Element) -> OptionConfiguration:
    out: OptionConfiguration = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_option_version = el.find("OptionVersion")
    if child_option_version is not None:
        out["option_version"] = str(child_option_version.text or "")
    child_db_security_group_memberships = el.find("DBSecurityGroupMemberships")
    if child_db_security_group_memberships is not None:
        import aws_sdk_rds.types.db_security_group_name_list

        out["db_security_group_memberships"] = (
            aws_sdk_rds.types.db_security_group_name_list.deserialize_query(
                child_db_security_group_memberships
            )
        )
    child_vpc_security_group_memberships = el.find("VpcSecurityGroupMemberships")
    if child_vpc_security_group_memberships is not None:
        import aws_sdk_rds.types.vpc_security_group_id_list

        out["vpc_security_group_memberships"] = (
            aws_sdk_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_memberships
            )
        )
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import aws_sdk_rds.types.option_settings_list

        out["option_settings"] = (
            aws_sdk_rds.types.option_settings_list.deserialize_query(
                child_option_settings
            )
        )
    return out
