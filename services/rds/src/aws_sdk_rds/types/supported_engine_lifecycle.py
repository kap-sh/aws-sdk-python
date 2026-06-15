"""Generated from Smithy shape ``com.amazonaws.rds#SupportedEngineLifecycle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.lifecycle_support_name
    import aws_sdk_rds.types.t_stamp


class SupportedEngineLifecycle(TypedDict):
    lifecycle_support_name: NotRequired[
        "aws_sdk_rds.types.lifecycle_support_name.LifecycleSupportName"
    ]
    r"""<p>The type of lifecycle support that the engine version is in.</p> <p>This parameter returns the following values:</p> <ul> <li> <p> <code>open-source-rds-standard-support</code> - Indicates RDS standard support or Aurora standard support.</p> </li> <li> <p> <code>open-source-rds-extended-support</code> - Indicates Amazon RDS Extended Support.</p> </li> </ul> <p>For Amazon RDS for MySQL, Amazon RDS for PostgreSQL, Aurora MySQL, and Aurora PostgreSQL, this parameter returns both <code>open-source-rds-standard-support</code> and <code>open-source-rds-extended-support</code>.</p> <p>For Amazon RDS for MariaDB, this parameter only returns the value <code>open-source-rds-standard-support</code>.</p> <p>For information about Amazon RDS Extended Support, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html\">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i> and <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html\">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    lifecycle_support_start_date: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The start date for the type of support returned by <code>LifecycleSupportName</code>.</p>"""
    lifecycle_support_end_date: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The end date for the type of support returned by <code>LifecycleSupportName</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedEngineLifecycle, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "lifecycle_support_name" in value:
        import aws_sdk_rds.types.lifecycle_support_name

        aws_sdk_rds.types.lifecycle_support_name.serialize_query(
            value["lifecycle_support_name"], pairs, f"{prefix}.LifecycleSupportName"
        )
    if "lifecycle_support_start_date" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["lifecycle_support_start_date"],
            pairs,
            f"{prefix}.LifecycleSupportStartDate",
        )
    if "lifecycle_support_end_date" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["lifecycle_support_end_date"],
            pairs,
            f"{prefix}.LifecycleSupportEndDate",
        )


def deserialize_query(el: Element) -> SupportedEngineLifecycle:
    out: SupportedEngineLifecycle = {}  # type: ignore[typeddict-item]
    child_lifecycle_support_name = el.find("LifecycleSupportName")
    if child_lifecycle_support_name is not None:
        import aws_sdk_rds.types.lifecycle_support_name

        out["lifecycle_support_name"] = (
            aws_sdk_rds.types.lifecycle_support_name.deserialize_query(
                child_lifecycle_support_name
            )
        )
    child_lifecycle_support_start_date = el.find("LifecycleSupportStartDate")
    if child_lifecycle_support_start_date is not None:
        import aws_sdk_rds.types.t_stamp

        out["lifecycle_support_start_date"] = (
            aws_sdk_rds.types.t_stamp.deserialize_query(
                child_lifecycle_support_start_date
            )
        )
    child_lifecycle_support_end_date = el.find("LifecycleSupportEndDate")
    if child_lifecycle_support_end_date is not None:
        import aws_sdk_rds.types.t_stamp

        out["lifecycle_support_end_date"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_lifecycle_support_end_date
        )
    return out
