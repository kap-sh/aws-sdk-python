"""Generated from Smithy shape ``com.amazonaws.docdb#OrderableDBInstanceOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.availability_zone_list
    import aws_sdk_docdb.types.boolean
    import aws_sdk_docdb.types.string


class OrderableDBInstanceOption(TypedDict, closed=True):
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The engine type of an instance.</p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The engine version of an instance.</p>"""
    db_instance_class: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The instance class for an instance.</p>"""
    license_model: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The license model for an instance.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_docdb.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>A list of Availability Zones for an instance.</p>"""
    vpc: NotRequired["aws_sdk_docdb.types.boolean.Boolean"]
    """<p>Indicates whether an instance is in a virtual private cloud (VPC).</p>"""
    storage_type: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The storage type to associate with the DB cluster</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "db_instance_class" in value:
        pairs.append((f"{prefix}.DBInstanceClass", str(value["db_instance_class"])))
    if "license_model" in value:
        pairs.append((f"{prefix}.LicenseModel", str(value["license_model"])))
    if "availability_zones" in value:
        import aws_sdk_docdb.types.availability_zone_list

        aws_sdk_docdb.types.availability_zone_list.serialize_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )
    if "vpc" in value:
        pairs.append((f"{prefix}.Vpc", "true" if value["vpc"] else "false"))
    if "storage_type" in value:
        pairs.append((f"{prefix}.StorageType", str(value["storage_type"])))


def deserialize_query(el: Element) -> OrderableDBInstanceOption:
    out: OrderableDBInstanceOption = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import aws_sdk_docdb.types.availability_zone_list

        out["availability_zones"] = (
            aws_sdk_docdb.types.availability_zone_list.deserialize_query(
                child_availability_zones
            )
        )
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        out["vpc"] = (child_vpc.text or "").lower() == "true"
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    return out
