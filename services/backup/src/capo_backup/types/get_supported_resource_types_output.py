"""Generated from Smithy shape ``com.amazonaws.backup#GetSupportedResourceTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.resource_types


class GetSupportedResourceTypesOutput(TypedDict, closed=True):
    resource_types: NotRequired["capo_backup.types.resource_types.ResourceTypes"]
    """<p>Contains a string with the supported Amazon Web Services resource types:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSupportedResourceTypesOutput) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import capo_backup.types.resource_types

        out["ResourceTypes"] = capo_backup.types.resource_types.serialize_json(
            value["resource_types"]
        )
    return out


def deserialize_json(data: dict) -> GetSupportedResourceTypesOutput:
    out: GetSupportedResourceTypesOutput = {}  # type: ignore[typeddict-item]
    if "ResourceTypes" in data:
        import capo_backup.types.resource_types

        out["resource_types"] = capo_backup.types.resource_types.deserialize_json(
            data["ResourceTypes"]
        )
    return out
