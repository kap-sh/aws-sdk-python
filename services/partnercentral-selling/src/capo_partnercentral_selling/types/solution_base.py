"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionBase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.solution_arn
    import capo_partnercentral_selling.types.solution_identifier
    import capo_partnercentral_selling.types.solution_status


class SolutionBase(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the solution is hosted, either <code>AWS</code> or <code>Sandbox</code>. This helps partners differentiate between live solutions and those in testing environments.</p>"""
    id: "capo_partnercentral_selling.types.solution_identifier.SolutionIdentifier"
    """<p>Enables the association of solutions (offerings) to opportunities.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.solution_arn.SolutionArn"]
    """<p> The SolutionBase structure provides essential information about a solution. </p>"""
    name: "str"
    """<p>Specifies the solution name.</p>"""
    status: "capo_partnercentral_selling.types.solution_status.SolutionStatus"
    """<p>Specifies the solution's current status, which indicates its state in the system. Valid values: <code>Active</code> | <code>Inactive</code> | <code>Draft</code>. The status helps partners and Amazon Web Services track the solution's lifecycle and availability. Filter for <code>Active</code> solutions for association to an opportunity.</p>"""
    category: "str"
    """<p>Specifies the solution category, which helps to categorize and organize the solutions partners offer. Valid values: <code>Software Product</code> | <code>Consulting Service</code> | <code>Hardware Product</code> | <code>Communications Product</code> | <code>Professional Service</code> | <code>Managed Service</code> | <code>Value-Added Resale Amazon Web Services Service</code> | <code>Distribution Service</code> | <code>Training Service</code> | <code>Merger and Acquisition Advising Service</code>.</p>"""
    created_date: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>Indicates the solution creation date. This is useful to track and audit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionBase) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import capo_partnercentral_selling.types.solution_status

    out["Status"] = (
        capo_partnercentral_selling.types.solution_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["Category"] = value["category"]
    import capo_partnercentral_selling.types.date_time

    out["CreatedDate"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SolutionBase:
    out: SolutionBase = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("SolutionBase.catalog required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SolutionBase.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SolutionBase.name required")
    if "Status" in data:
        import capo_partnercentral_selling.types.solution_status

        out["status"] = (
            capo_partnercentral_selling.types.solution_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("SolutionBase.status required")
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError("SolutionBase.category required")
    if "CreatedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["created_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    else:
        raise DeserializationError("SolutionBase.created_date required")
    return out
