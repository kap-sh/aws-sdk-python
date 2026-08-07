"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeploymentTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_filter_type
    import capo_cloudformation.types.account_list
    import capo_cloudformation.types.accounts_url
    import capo_cloudformation.types.organizational_unit_id_list


class DeploymentTargets(TypedDict, closed=True):
    accounts: NotRequired["capo_cloudformation.types.account_list.AccountList"]
    """<p>The Amazon Web Services account IDs where you want to perform stack operations. How these accounts are used depends on the <code>AccountFilterType</code> property.</p> <p>If you have many account numbers, you can provide those accounts using the <code>AccountsUrl</code> property instead.</p>"""
    accounts_url: NotRequired["capo_cloudformation.types.accounts_url.AccountsUrl"]
    """<p>The Amazon S3 URL path to a file that contains a list of Amazon Web Services account IDs. The file format must be either <code>.csv</code> or <code>.txt</code>, and the data can be comma-separated or new-line-separated. There is currently a 10MB limit for the data (approximately 800,000 accounts).</p> <p>This property serves the same purpose as <code>Accounts</code> but allows you to specify a large number of accounts.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_cloudformation.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The organization root ID or organizational unit (OU) IDs where you want to perform stack operations. CloudFormation will perform operations on accounts within these OUs and their child OUs.</p>"""
    account_filter_type: NotRequired[
        "capo_cloudformation.types.account_filter_type.AccountFilterType"
    ]
    """<p>Refines which accounts will have stack operations performed on them by specifying how to use the <code>Accounts</code> and <code>OrganizationalUnitIds</code> properties together.</p> <p>The following values determine how CloudFormation selects target accounts:</p> <ul> <li> <p> <code>INTERSECTION</code>: Performs stack operations only on specific individual accounts within the selected OUs. Only accounts that are both specified in the <code>Accounts</code> property and belong to the specified OUs will be targeted.</p> </li> <li> <p> <code>DIFFERENCE</code>: Performs stack operations on all accounts in the selected OUs except for specific accounts listed in the <code>Accounts</code> property. This enables you to exclude certain accounts within an OU, such as suspended accounts.</p> </li> <li> <p> <code>UNION</code>: Performs stack operations on the specified OUs plus additional individual accounts listed in the <code>Accounts</code> property. This is the default value if <code>AccountFilterType</code> is not provided. This lets you target an entire OU and individual accounts from a different OU in one request. Note that <code>UNION</code> is not supported for <code>CreateStackInstances</code> operations.</p> </li> <li> <p> <code>NONE</code>: Performs stack operations on all accounts in the specified organizational units (OUs).</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeploymentTargets, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "accounts" in value:
        import capo_cloudformation.types.account_list

        capo_cloudformation.types.account_list.serialize_query(
            value["accounts"], pairs, f"{key_prefix}Accounts"
        )
    if "accounts_url" in value:
        pairs.append((f"{key_prefix}AccountsUrl", str(value["accounts_url"])))
    if "organizational_unit_ids" in value:
        import capo_cloudformation.types.organizational_unit_id_list

        capo_cloudformation.types.organizational_unit_id_list.serialize_query(
            value["organizational_unit_ids"],
            pairs,
            f"{key_prefix}OrganizationalUnitIds",
        )
    if "account_filter_type" in value:
        import capo_cloudformation.types.account_filter_type

        capo_cloudformation.types.account_filter_type.serialize_query(
            value["account_filter_type"], pairs, f"{key_prefix}AccountFilterType"
        )


def deserialize_query(el: Element) -> DeploymentTargets:
    out: DeploymentTargets = {}  # type: ignore[typeddict-item]
    child_accounts = el.find("Accounts")
    if child_accounts is not None:
        import capo_cloudformation.types.account_list

        out["accounts"] = capo_cloudformation.types.account_list.deserialize_query(
            child_accounts
        )
    child_accounts_url = el.find("AccountsUrl")
    if child_accounts_url is not None:
        out["accounts_url"] = str(child_accounts_url.text or "")
    child_organizational_unit_ids = el.find("OrganizationalUnitIds")
    if child_organizational_unit_ids is not None:
        import capo_cloudformation.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_cloudformation.types.organizational_unit_id_list.deserialize_query(
                child_organizational_unit_ids
            )
        )
    child_account_filter_type = el.find("AccountFilterType")
    if child_account_filter_type is not None:
        import capo_cloudformation.types.account_filter_type

        out["account_filter_type"] = (
            capo_cloudformation.types.account_filter_type.deserialize_query(
                child_account_filter_type
            )
        )
    return out
