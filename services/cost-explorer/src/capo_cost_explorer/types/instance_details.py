"""Generated from Smithy shape ``com.amazonaws.costexplorer#InstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.ec2_instance_details
    import capo_cost_explorer.types.elasti_cache_instance_details
    import capo_cost_explorer.types.es_instance_details
    import capo_cost_explorer.types.memory_db_instance_details
    import capo_cost_explorer.types.rds_instance_details
    import capo_cost_explorer.types.redshift_instance_details


class InstanceDetails(TypedDict, closed=True):
    ec2_instance_details: NotRequired[
        "capo_cost_explorer.types.ec2_instance_details.EC2InstanceDetails"
    ]
    """<p>The Amazon EC2 reservations that Amazon Web Services recommends that you purchase.</p>"""
    rds_instance_details: NotRequired[
        "capo_cost_explorer.types.rds_instance_details.RDSInstanceDetails"
    ]
    """<p>The Amazon RDS reservations that Amazon Web Services recommends that you purchase.</p>"""
    redshift_instance_details: NotRequired[
        "capo_cost_explorer.types.redshift_instance_details.RedshiftInstanceDetails"
    ]
    """<p>The Amazon Redshift reservations that Amazon Web Services recommends that you purchase.</p>"""
    elasti_cache_instance_details: NotRequired[
        "capo_cost_explorer.types.elasti_cache_instance_details.ElastiCacheInstanceDetails"
    ]
    """<p>The ElastiCache reservations that Amazon Web Services recommends that you purchase.</p>"""
    es_instance_details: NotRequired[
        "capo_cost_explorer.types.es_instance_details.ESInstanceDetails"
    ]
    """<p>The Amazon OpenSearch Service reservations that Amazon Web Services recommends that you purchase.</p>"""
    memory_db_instance_details: NotRequired[
        "capo_cost_explorer.types.memory_db_instance_details.MemoryDBInstanceDetails"
    ]
    """<p>The MemoryDB reservations that Amazon Web Services recommends that you purchase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceDetails) -> dict:
    out: dict = {}
    if "ec2_instance_details" in value:
        import capo_cost_explorer.types.ec2_instance_details

        out["EC2InstanceDetails"] = (
            capo_cost_explorer.types.ec2_instance_details.serialize_aws_json_1_1(
                value["ec2_instance_details"]
            )
        )
    if "rds_instance_details" in value:
        import capo_cost_explorer.types.rds_instance_details

        out["RDSInstanceDetails"] = (
            capo_cost_explorer.types.rds_instance_details.serialize_aws_json_1_1(
                value["rds_instance_details"]
            )
        )
    if "redshift_instance_details" in value:
        import capo_cost_explorer.types.redshift_instance_details

        out["RedshiftInstanceDetails"] = (
            capo_cost_explorer.types.redshift_instance_details.serialize_aws_json_1_1(
                value["redshift_instance_details"]
            )
        )
    if "elasti_cache_instance_details" in value:
        import capo_cost_explorer.types.elasti_cache_instance_details

        out["ElastiCacheInstanceDetails"] = (
            capo_cost_explorer.types.elasti_cache_instance_details.serialize_aws_json_1_1(
                value["elasti_cache_instance_details"]
            )
        )
    if "es_instance_details" in value:
        import capo_cost_explorer.types.es_instance_details

        out["ESInstanceDetails"] = (
            capo_cost_explorer.types.es_instance_details.serialize_aws_json_1_1(
                value["es_instance_details"]
            )
        )
    if "memory_db_instance_details" in value:
        import capo_cost_explorer.types.memory_db_instance_details

        out["MemoryDBInstanceDetails"] = (
            capo_cost_explorer.types.memory_db_instance_details.serialize_aws_json_1_1(
                value["memory_db_instance_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceDetails:
    out: InstanceDetails = {}  # type: ignore[typeddict-item]
    if "EC2InstanceDetails" in data:
        import capo_cost_explorer.types.ec2_instance_details

        out["ec2_instance_details"] = (
            capo_cost_explorer.types.ec2_instance_details.deserialize_aws_json_1_1(
                data["EC2InstanceDetails"]
            )
        )
    if "RDSInstanceDetails" in data:
        import capo_cost_explorer.types.rds_instance_details

        out["rds_instance_details"] = (
            capo_cost_explorer.types.rds_instance_details.deserialize_aws_json_1_1(
                data["RDSInstanceDetails"]
            )
        )
    if "RedshiftInstanceDetails" in data:
        import capo_cost_explorer.types.redshift_instance_details

        out["redshift_instance_details"] = (
            capo_cost_explorer.types.redshift_instance_details.deserialize_aws_json_1_1(
                data["RedshiftInstanceDetails"]
            )
        )
    if "ElastiCacheInstanceDetails" in data:
        import capo_cost_explorer.types.elasti_cache_instance_details

        out["elasti_cache_instance_details"] = (
            capo_cost_explorer.types.elasti_cache_instance_details.deserialize_aws_json_1_1(
                data["ElastiCacheInstanceDetails"]
            )
        )
    if "ESInstanceDetails" in data:
        import capo_cost_explorer.types.es_instance_details

        out["es_instance_details"] = (
            capo_cost_explorer.types.es_instance_details.deserialize_aws_json_1_1(
                data["ESInstanceDetails"]
            )
        )
    if "MemoryDBInstanceDetails" in data:
        import capo_cost_explorer.types.memory_db_instance_details

        out["memory_db_instance_details"] = (
            capo_cost_explorer.types.memory_db_instance_details.deserialize_aws_json_1_1(
                data["MemoryDBInstanceDetails"]
            )
        )
    return out
