"""Generated from Smithy shape ``com.amazonaws.ssm#Patch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.patch_advisory_id_list
    import capo_ssm.types.patch_arch
    import capo_ssm.types.patch_bugzilla_id_list
    import capo_ssm.types.patch_classification
    import capo_ssm.types.patch_content_url
    import capo_ssm.types.patch_cve_id_list
    import capo_ssm.types.patch_description
    import capo_ssm.types.patch_epoch
    import capo_ssm.types.patch_id
    import capo_ssm.types.patch_kb_number
    import capo_ssm.types.patch_language
    import capo_ssm.types.patch_msrc_number
    import capo_ssm.types.patch_msrc_severity
    import capo_ssm.types.patch_name
    import capo_ssm.types.patch_product
    import capo_ssm.types.patch_product_family
    import capo_ssm.types.patch_release
    import capo_ssm.types.patch_repository
    import capo_ssm.types.patch_severity
    import capo_ssm.types.patch_title
    import capo_ssm.types.patch_vendor
    import capo_ssm.types.patch_version


class Patch(TypedDict, closed=True):
    id: NotRequired["capo_ssm.types.patch_id.PatchId"]
    """<p>The ID of the patch. Applies to Windows patches only.</p> <note> <p>This ID isn't the same as the Microsoft Knowledge Base ID.</p> </note>"""
    release_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the patch was released.</p>"""
    title: NotRequired["capo_ssm.types.patch_title.PatchTitle"]
    """<p>The title of the patch.</p>"""
    description: NotRequired["capo_ssm.types.patch_description.PatchDescription"]
    """<p>The description of the patch.</p>"""
    content_url: NotRequired["capo_ssm.types.patch_content_url.PatchContentUrl"]
    """<p>The URL where more information can be obtained about the patch.</p>"""
    vendor: NotRequired["capo_ssm.types.patch_vendor.PatchVendor"]
    """<p>The name of the vendor providing the patch.</p>"""
    product_family: NotRequired[
        "capo_ssm.types.patch_product_family.PatchProductFamily"
    ]
    """<p>The product family the patch is applicable for. For example, <code>Windows</code> or <code>Amazon Linux 2</code>.</p>"""
    product: NotRequired["capo_ssm.types.patch_product.PatchProduct"]
    """<p>The specific product the patch is applicable for. For example, <code>WindowsServer2016</code> or <code>AmazonLinux2018.03</code>.</p>"""
    classification: NotRequired[
        "capo_ssm.types.patch_classification.PatchClassification"
    ]
    """<p>The classification of the patch. For example, <code>SecurityUpdates</code>, <code>Updates</code>, or <code>CriticalUpdates</code>.</p>"""
    msrc_severity: NotRequired["capo_ssm.types.patch_msrc_severity.PatchMsrcSeverity"]
    """<p>The severity of the patch, such as <code>Critical</code>, <code>Important</code>, or <code>Moderate</code>. Applies to Windows patches only.</p>"""
    kb_number: NotRequired["capo_ssm.types.patch_kb_number.PatchKbNumber"]
    """<p>The Microsoft Knowledge Base ID of the patch. Applies to Windows patches only.</p>"""
    msrc_number: NotRequired["capo_ssm.types.patch_msrc_number.PatchMsrcNumber"]
    """<p>The ID of the Microsoft Security Response Center (MSRC) bulletin the patch is related to. For example, <code>MS14-045</code>. Applies to Windows patches only.</p>"""
    language: NotRequired["capo_ssm.types.patch_language.PatchLanguage"]
    """<p>The language of the patch if it's language-specific.</p>"""
    advisory_ids: NotRequired[
        "capo_ssm.types.patch_advisory_id_list.PatchAdvisoryIdList"
    ]
    """<p>The Advisory ID of the patch. For example, <code>RHSA-2020:3779</code>. Applies to Linux-based managed nodes only.</p>"""
    bugzilla_ids: NotRequired[
        "capo_ssm.types.patch_bugzilla_id_list.PatchBugzillaIdList"
    ]
    """<p>The Bugzilla ID of the patch. For example, <code>1600646</code>. Applies to Linux-based managed nodes only.</p>"""
    cve_ids: NotRequired["capo_ssm.types.patch_cve_id_list.PatchCVEIdList"]
    """<p>The Common Vulnerabilities and Exposures (CVE) ID of the patch. For example, <code>CVE-2011-3192</code>. Applies to Linux-based managed nodes only.</p>"""
    name: NotRequired["capo_ssm.types.patch_name.PatchName"]
    """<p>The name of the patch. Applies to Linux-based managed nodes only.</p>"""
    epoch: "capo_ssm.types.patch_epoch.PatchEpoch"
    """<p>The epoch of the patch. For example in <code>pkg-example-EE-20180914-2.2.amzn1.noarch</code>, the epoch value is <code>20180914-2</code>. Applies to Linux-based managed nodes only.</p>"""
    version: NotRequired["capo_ssm.types.patch_version.PatchVersion"]
    """<p>The version number of the patch. For example, in <code>example-pkg-1.710.10-2.7.abcd.x86_64</code>, the version number is indicated by <code>-1</code>. Applies to Linux-based managed nodes only.</p>"""
    release: NotRequired["capo_ssm.types.patch_release.PatchRelease"]
    """<p>The particular release of a patch. For example, in <code>pkg-example-EE-20180914-2.2.amzn1.noarch</code>, the release is <code>2.amaz1</code>. Applies to Linux-based managed nodes only.</p>"""
    arch: NotRequired["capo_ssm.types.patch_arch.PatchArch"]
    """<p>The architecture of the patch. For example, in <code>example-pkg-0.710.10-2.7.abcd.x86_64</code>, the architecture is indicated by <code>x86_64</code>. Applies to Linux-based managed nodes only.</p>"""
    severity: NotRequired["capo_ssm.types.patch_severity.PatchSeverity"]
    """<p>The severity level of the patch. For example, <code>CRITICAL</code> or <code>MODERATE</code>.</p>"""
    repository: NotRequired["capo_ssm.types.patch_repository.PatchRepository"]
    """<p>The source patch repository for the operating system and version, such as <code>trusty-security</code> for Ubuntu Server 14.04 LTE and <code>focal-security</code> for Ubuntu Server 20.04 LTE. Applies to Linux-based managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Patch) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "release_date" in value:
        import capo_ssm.types.date_time

        out["ReleaseDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["release_date"]
        )
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "content_url" in value:
        out["ContentUrl"] = value["content_url"]
    if "vendor" in value:
        out["Vendor"] = value["vendor"]
    if "product_family" in value:
        out["ProductFamily"] = value["product_family"]
    if "product" in value:
        out["Product"] = value["product"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "msrc_severity" in value:
        out["MsrcSeverity"] = value["msrc_severity"]
    if "kb_number" in value:
        out["KbNumber"] = value["kb_number"]
    if "msrc_number" in value:
        out["MsrcNumber"] = value["msrc_number"]
    if "language" in value:
        out["Language"] = value["language"]
    if "advisory_ids" in value:
        import capo_ssm.types.patch_advisory_id_list

        out["AdvisoryIds"] = (
            capo_ssm.types.patch_advisory_id_list.serialize_aws_json_1_1(
                value["advisory_ids"]
            )
        )
    if "bugzilla_ids" in value:
        import capo_ssm.types.patch_bugzilla_id_list

        out["BugzillaIds"] = (
            capo_ssm.types.patch_bugzilla_id_list.serialize_aws_json_1_1(
                value["bugzilla_ids"]
            )
        )
    if "cve_ids" in value:
        import capo_ssm.types.patch_cve_id_list

        out["CVEIds"] = capo_ssm.types.patch_cve_id_list.serialize_aws_json_1_1(
            value["cve_ids"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    out["Epoch"] = value.get("epoch", 0)
    if "version" in value:
        out["Version"] = value["version"]
    if "release" in value:
        out["Release"] = value["release"]
    if "arch" in value:
        out["Arch"] = value["arch"]
    if "severity" in value:
        out["Severity"] = value["severity"]
    if "repository" in value:
        out["Repository"] = value["repository"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Patch:
    out: Patch = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ReleaseDate") is not None:
        import capo_ssm.types.date_time

        out["release_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ReleaseDate"]
        )
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContentUrl") is not None:
        out["content_url"] = data["ContentUrl"]
    if data.get("Vendor") is not None:
        out["vendor"] = data["Vendor"]
    if data.get("ProductFamily") is not None:
        out["product_family"] = data["ProductFamily"]
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("MsrcSeverity") is not None:
        out["msrc_severity"] = data["MsrcSeverity"]
    if data.get("KbNumber") is not None:
        out["kb_number"] = data["KbNumber"]
    if data.get("MsrcNumber") is not None:
        out["msrc_number"] = data["MsrcNumber"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("AdvisoryIds") is not None:
        import capo_ssm.types.patch_advisory_id_list

        out["advisory_ids"] = (
            capo_ssm.types.patch_advisory_id_list.deserialize_aws_json_1_1(
                data["AdvisoryIds"]
            )
        )
    if data.get("BugzillaIds") is not None:
        import capo_ssm.types.patch_bugzilla_id_list

        out["bugzilla_ids"] = (
            capo_ssm.types.patch_bugzilla_id_list.deserialize_aws_json_1_1(
                data["BugzillaIds"]
            )
        )
    if data.get("CVEIds") is not None:
        import capo_ssm.types.patch_cve_id_list

        out["cve_ids"] = capo_ssm.types.patch_cve_id_list.deserialize_aws_json_1_1(
            data["CVEIds"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Epoch") is not None:
        out["epoch"] = data["Epoch"]
    else:
        out["epoch"] = 0
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Release") is not None:
        out["release"] = data["Release"]
    if data.get("Arch") is not None:
        out["arch"] = data["Arch"]
    if data.get("Severity") is not None:
        out["severity"] = data["Severity"]
    if data.get("Repository") is not None:
        out["repository"] = data["Repository"]
    return out
